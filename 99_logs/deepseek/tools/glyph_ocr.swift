// glyph_ocr.swift — 对单字符 PNG 做 Vision OCR, 输出候选字符与置信度
// 用法: swift glyph_ocr.swift <png目录> <输出json路径>
import Foundation
import Vision
import AppKit

func ocrImage(_ path: String) -> [[String: Any]] {
    guard let img = NSImage(contentsOfFile: path),
          let cg = img.cgImage(forProposedRect: nil, context: nil, hints: nil) else { return [] }
    let request = VNRecognizeTextRequest()
    request.recognitionLevel = .accurate
    request.recognitionLanguages = ["zh-Hans", "zh-Hant"]
    request.usesLanguageCorrection = false
    let handler = VNImageRequestHandler(cgImage: cg, options: [:])
    try? handler.perform([request])
    var out: [[String: Any]] = []
    for obs in (request.results ?? []) {
        for c in obs.topCandidates(3) {
            out.append(["text": String(c.string), "conf": c.confidence])
        }
    }
    return out
}

let args = CommandLine.arguments
let dir = args[1], outPath = args[2]
var result: [String: Any] = [:]
let files = (try? FileManager.default.contentsOfDirectory(atPath: dir))?.filter { $0.hasSuffix(".png") } ?? []
for f in files.sorted() {
    let key = (f as NSString).deletingPathExtension
    result[key] = ocrImage(dir + "/" + f)
}
let data = try! JSONSerialization.data(withJSONObject: result)
try! data.write(to: URL(fileURLWithPath: outPath))
