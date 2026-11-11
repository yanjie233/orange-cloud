//
//  AboutView.swift
//  Orange Cloud
//
//  「关于」二级页：版本、社区（Telegram 频道）、署名。自编译版已去掉评分 / GitHub / 隐私 / 条款四个外链。
//  设置根页只保留单个「关于」入口，避免根页堆积过多外链。
//

import SwiftUI

struct AboutView: View {

    private var appVersion: String {
        let version = Bundle.main.infoDictionary?["CFBundleShortVersionString"] as? String ?? "1.0"
        let build = Bundle.main.infoDictionary?["CFBundleVersion"] as? String ?? "1"
        return "\(version) (\(build))"
    }

    var body: some View {
        List {
            // ── App 头部 ──
            Section {
                VStack(spacing: 8) {
                    Image(systemName: "cloud.fill")
                        .font(.system(size: 44))
                        .foregroundStyle(Color.ocOrange)
                        .accessibilityHidden(true)
                    Text(verbatim: "Orange Cloud")
                        .font(.title2.bold())
                    Text(appVersion)
                        .font(.callout)
                        .foregroundStyle(.secondary)
                        .textSelection(.enabled)
                    Text("第三方 Cloudflare 客户端")
                        .font(.caption)
                        .foregroundStyle(.tertiary)
                }
                .frame(maxWidth: .infinity)
                .padding(.vertical, 8)
                .listRowBackground(Color.clear)
            }

            // ── 社区 ──
            Section {
                aboutLink(String(localized: "Telegram 频道"), icon: "paperplane", url: "https://t.me/orange_cloud_channel")
            } header: {
                Text("社区")
            } footer: {
                Text("Telegram 频道发布版本更新与项目动态。")
            }
            .glassRow()

            // ── 署名（自编译版去掉评分 / GitHub / 隐私 / 条款四个外链，只留署名） ──
            Section {
                VStack(spacing: 4) {
                    Text("Orange Cloud · 第三方 Cloudflare 客户端")
                    Text("@ Yanjie233")
                }
                .font(.footnote)
                .foregroundStyle(.secondary)
                .frame(maxWidth: .infinity, alignment: .center)
                .padding(.vertical, 8)
            }
            .glassRow()
        }
        .daybreakList()
        .navigationTitle("关于")
        .navigationBarTitleDisplayMode(.inline)
    }

    private func aboutLink(_ title: String, icon: String, url: String) -> some View {
        Link(destination: URL(string: url)!) {
            HStack(spacing: 12) {
                TintIcon(systemImage: icon, color: .gray)
                Text(title)
                    .foregroundStyle(.primary)
                Spacer()
                Image(systemName: "arrow.up.right")
                    .font(.caption)
                    .foregroundStyle(.tertiary)
            }
        }
    }
}
