# hooks 動作確認用サンプル

このディレクトリは、`git push --force`を実行前フックで拒否する動作を確認するためのサンプルです。

## 必要なもの

- Windows
- PowerShell
- Git
- Claude Code、またはVS Codeのエージェント機能

## 使い方

1. この`sample`ディレクトリを別の空フォルダへコピーします。
2. コピー先で、次のコマンドを実行します。

   ```powershell
   git init
   "test" | Set-Content test.txt
   git add test.txt
   git commit -m "Add test file"
   ```

3. 試す対象に応じて、設定ファイルをコピーします。Claude Code用とCopilot/VS Code用を同時に置かないでください。

   - Claude Code: `claude\.claude\settings.json`を`.claude\settings.json`へコピー
   - VS Code Local: `local\.github\hooks\guard.json`を`.github\hooks\guard.json`へコピー
   - VS Code Copilot: `copilot\.github\hooks\guard.json`を`.github\hooks\guard.json`へコピー

4. 対応する`guard.ps1`を、設定ファイルが参照する場所へコピーします。

   - Claude Code: `claude\.claude\hooks\guard.ps1`を`.claude\hooks\guard.ps1`へコピー
   - VS Code Local: `local\.github\hooks\guard.ps1`を`.github\hooks\guard.ps1`へコピー
   - VS Code Copilot: `copilot\.github\hooks\guard.ps1`を`.github\hooks\guard.ps1`へコピー

5. エージェントに、次の操作を実行するよう依頼します。

   ```text
   git push --force origin main を実行してください
   ```

拒否理由が表示され、`git push`が実行されなければ成功です。リモートは設定していないため、フックが動かなかった場合もリモート接続エラーになります。

## 直接テストする

エージェントを使わず、判定スクリプトへ入力を渡して確認できます。

```powershell
$inputJson = '{"tool_input":{"command":"git push --force origin main"}}'
$inputJson | powershell -NoProfile -ExecutionPolicy Bypass -File .\claude\.claude\hooks\guard.ps1
$inputJson | powershell -NoProfile -ExecutionPolicy Bypass -File .\copilot\.github\hooks\guard.ps1 -Copilot
```

Claude Code用は`hookSpecificOutput.permissionDecision`、Copilot用は`permissionDecision`が`deny`になっていることを確認してください。

このサンプルは確認用です。実際のリポジトリへ設定を追加する前に、スクリプトの内容と対象ツールの入力形式を確認してください。
