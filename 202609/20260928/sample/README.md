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
   git branch -M main
   ```

   `git init`直後のブランチ名は、環境によって`master`になっていることがあります。以降の手順では`main`を使うため、ここで明示的にリネームします。

3. コピー先の親ディレクトリで、ローカル用のbareリポジトリを作成します。次の例では、確認用フォルダの隣に`hooks-test-remote.git`を作ります。

   ```powershell
   New-Item -ItemType Directory ..\hooks-test-remote.git -Force | Out-Null
   git -C ..\hooks-test-remote.git init --bare --shared
   git remote add origin ..\hooks-test-remote.git
   ```

   `--bare`は作業ツリーを持たないリモート用リポジトリを作成するオプションです。`--shared`は、ローカルの複数ユーザーで共有できる権限設定を行います。単独で試す場合は`git init --bare`でも構いません。

4. リモートへの接続とブランチ名を確認します。

   ```powershell
   git remote -v
   git branch --show-current
   ```

   `origin`が`..\hooks-test-remote.git`を指し、ブランチ名が`main`になっていれば準備完了です。フックを確認する前に、通常のpushが成功することも確認できます。

   ```powershell
   git push -u origin main
   ```

5. 試す対象に応じて、設定ファイルをコピーします。Claude Code用とCopilot/VS Code用を同時に置かないでください。

   - Claude Code: `claude\.claude\settings.json`を`.claude\settings.json`へコピー
   - VS Code Local: `local\.github\hooks\guard.json`を`.github\hooks\guard.json`へコピー
   - VS Code Copilot: `copilot\.github\hooks\guard.json`を`.github\hooks\guard.json`へコピー

6. 対応する`guard.ps1`を、設定ファイルが参照する場所へコピーします。

   - Claude Code: `claude\.claude\hooks\guard.ps1`を`.claude\hooks\guard.ps1`へコピー
   - VS Code Local: `local\.github\hooks\guard.ps1`を`.github\hooks\guard.ps1`へコピー
   - VS Code Copilot: `copilot\.github\hooks\guard.ps1`を`.github\hooks\guard.ps1`へコピー

7. エージェントに、次の操作を実行するよう依頼します。

   ```text
   git push --force origin main を実行してください
   ```

拒否理由が表示され、`git push`が実行されなければ成功です。フックが動かなかった場合は、ローカルのbareリポジトリにforce pushされます。

## 直接テストする

エージェントを使わず、判定スクリプトへ入力を渡して確認できます。

```powershell
$inputJson = '{"tool_input":{"command":"git push --force origin main"}}'
$inputJson | powershell -NoProfile -ExecutionPolicy Bypass -File .\claude\.claude\hooks\guard.ps1
$inputJson | powershell -NoProfile -ExecutionPolicy Bypass -File .\copilot\.github\hooks\guard.ps1 -Copilot
```

Claude Code用は`hookSpecificOutput.permissionDecision`、Copilot用は`permissionDecision`が`deny`になっていることを確認してください。

このサンプルは確認用です。実際のリポジトリへ設定を追加する前に、スクリプトの内容と対象ツールの入力形式を確認してください。
