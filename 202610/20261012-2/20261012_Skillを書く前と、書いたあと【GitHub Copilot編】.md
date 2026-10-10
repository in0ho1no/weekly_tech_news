---
html:
  embed_local_images: true
  embed_svg: true
  offline: true
  toc: true
export_on_save:
  html: true
---

# Skillを書く前と、書いたあと【GitHub Copilot編】

:::warning
業務でのAI利用は各所属のルールに従ってください。
:::

:::info
本書ではGitHub Copilot Chatを扱い、Copilot CLIは適用対象外となります。
:::

## きっかけ

### Skillを使い始めた人へ

先日の記事「その呼び方、AIは知っていますか」では、Skillの最小限の形（名前・description・本文）を紹介しました。  
実際にSkillを作り始めると、「思った場面で使われない」「書いた指示どおりに動かない」といった、もう一歩先の悩みが出てきます。  

本記事では、VS CodeのGitHub Copilot Chatで使うSkillを対象に、次の3つの場面を整理します。  

- 書く前：いきなり書かずに、エージェントと壁打ちして中身を固める
- 書くとき：先頭の`---`で囲まれた部分（front matter）で決められること
- 書いたあと：指示の矛盾や曖昧さを点検し、モデルが更新されたら見直す

読み終えると、自分のSkillを「作って終わり」にせず、手入れしながら使う流れがつかめます。  

:::caution
本記事は2026年10月10日時点の公式ドキュメントをもとに作成しています。
:::

## 書く前に固める

### いきなり書かせず、壁打ちする

Skillの不調は、書き方より前の段階、つまり「何をさせたいのか」が決まりきっていないことから起きる場合があります。  
そこで、Skillを書かせる前に、エージェントと会話しながら次の点を固めておきます。  

| 固めること | 曖昧なままだと起きやすいこと |
| --- | --- |
| 何をさせたいか（ゴール） | 本文が長くなり、指示同士がぶつかる |
| どんな依頼のときに使い、どんなときは使わないか | 使ってほしい場面で読み込まれない、関係ない場面で読み込まれる |
| 手順と、守ってほしい条件 | 毎回やり方が変わる |
| 自動で使わせるか、自分で呼び出すときだけにするか | 意図しない場面で動き出す |

2つ目はdescriptionに、4つ目はこの後で紹介するfront matterの項目に、そのままつながります。  

壁打ちは、たとえば次のように頼むと始めやすくなります。  

:::sample

```text
〇〇の作業をSkillにしたいと考えています。
まだSKILL.mdは書かないでください。
ゴール、使う場面と使わない場面、手順、守る条件を固めたいので、
足りない情報を1つずつ質問してください。
```

:::

内容が固まったら、その会話の流れでSkillを書かせます。  
VS Codeでは、同じチャットで`/create-skill`と入力し、「ここまでに固めた内容をもとにSkillを作ってください」と依頼する方法もあります。  

:::source
Generate a skill with AI
<https://code.visualstudio.com/docs/agent-customization/agent-skills#_generate-a-skill-with-ai>
:::

### ネット上のSkillは、そのまま使わない

公開されているSkillを見つけても、そのまま取り込んで使うことは避けます。  
以前の記事「それってライセンス大丈夫？」で整理したとおり、公開されていることと自由に使えることは別の話です。  

利用条件を確認したうえで、中身が自分の環境や目的に合うかを点検します。  
他人のSkillは、その人の環境・目的・使っていたモデルに合わせて書かれているため、必要な考え方だけを参考にして、自分の作業に合わせて書き直す方が、結果として扱いやすいSkillになります。  

## front matterで決められること

### 指定できる主な項目

Copilot ChatのSkillは、`.github/skills/<Skill名>/SKILL.md`のように、Skill名のフォルダの中に置きます。  
`SKILL.md`の先頭（front matter）では、次の項目を指定できます。  

| 項目 | 必須 | 内容 |
| --- | --- | --- |
| `name` | 必須 | 英小文字・数字・ハイフンのみ。親フォルダ名と一致させる。 |
| `description` | 必須 | 何をするSkillか、どんなときに使うか。 |
| `argument-hint` | 任意 | `/`でSkillを呼び出したとき、入力欄に表示されるヒント |
| `user-invocable` | 任意 | 既定は`true`。`false`にすると`/`のメニューに表示されない。（エージェントが自動で読み込むことはできる） |
| `disable-model-invocation` | 任意 | 既定は`false`。`true`にすると、`/`から自分で呼び出したときだけ使われる |

`name`に使えない文字が含まれていたり、フォルダ名と一致していなかったりすると、Skillは読み込まれません。  
「作ったはずのSkillが`/`のメニューに出てこない」ときは、まずここを確認します。  

「自分で呼び出すときだけ使う」と決めたSkillは、`disable-model-invocation: true`を指定しておくと、意図しない場面で動き出すことを防げます。  

:::sample

```markdown
---
name: weekly-report-draft
description: 週報の下書きを、決まった見出し構成で作る。週報を書くときに使う。
argument-hint: 対象の週（例：10/5〜10/9）
disable-model-invocation: true
---
```

:::

### モデルは指定できない

Copilot ChatのSkillには、使うモデルを指定する項目がありません。  
Skillは、そのときチャットで選ばれているモデルで動きます。  
そのため、同じSkillでも、選ぶモデルやモデルの更新によって振る舞いが変わることがあります。  

:::source
VS Code Docs「Use Agent Skills in VS Code」
<https://code.visualstudio.com/docs/copilot/customization/agent-skills>
:::

:::info
本書では扱いませんが、カスタムエージェントではモデルを指定できます。
どうしても特定のモデルにSkillを利用させたい場合、カスタムエージェント経由でSkillを使わせることになります。
:::
