# 授業用Laravel環境について

**このテキストの文章は、課題作成時に適宜書き換えてください**

このディレクトリは、授業用のLaravel環境です。
利用の際は、以下の注意点を意識しておいてください。

## コンテナ構成

このシステムでは、以下の構成で動くようコンテナが設定されています。

* appコンテナ
  * PHPの動く部分です
* webコンテナ
  * Webサーバーの動く部分です
  * appコンテナに対するフロントエンド(リバースプロキシ)にもなっています
  * publicのディレクトリしか見えません
* dbコンテナ
  * データベース部分です(MySQL)
  * 主にappコンテナから利用されます
  * 接続情報は `env.txt` に記載されています
* phpmyadminコンテナ(データベースの管理用)
  * 開発コンテナー使用時のみ起動します
* seleniumコンテナ(テスト環境のみ)
  * 評価環境使用時のみ起動します

## 利用方法

1. リポジトリのクローン
   - このリポジトリをcloneしてください(GitHub Classroomからアサインされていればあなた用です)
2. 開発コンテナを起動する
    - vscodeにて『PHP開発環境』で起動してください
3. `.env` の作成
    - 指示に従い作成しましょう(授業内で指示があります)

Laravel環境の初期設定は、授業にて説明があるので、それにしたがってください。
初期設定ができていないと、単純なPHPページは表示できるかもしれませんが、Laravelのアプリケーションは(ほぼ)動きません。

## 課題の提出方法

ローカル(開発コンテナ上)での作業が終わったら、従来通りGitHub上にPushすれば完了で、自動採点がはじまります。
ただし、GitHub Classroomの仕様上、以下の作業を事前に行わないと **自動採点ができない** ので、以下の対応を忘れずに行ってください。

### GitHub Secretsの登録

Laravelの設定上、`.env`ファイルをGitHubに送信できないようにされています。
そのため、GitHubのSecrets機能を利用して、`.env`ファイルの内容をGitHubに登録してください。

1. GitHubのリポジトリのページに移動
2. Settingsをクリック
3. Security項目の **Secrets and variables** をクリック

これで現在登録済みのSecretsが表示されます(初期状態では空っぽ)。
ここで以下の内容を登録してください(`New repository secret`ボタンから登録できます)。。

* キー名: `DOTENV`
* 値: `.env`ファイルの内容をそのまま貼り付け

この設定で保存することで、自動採点の時に、`.env`ファイルを生成します。

なお、開発コンテナ内で `gh`コマンドが有効な場合、以下の操作で現在の `.env` の内容を登録できます。

```bash
$ gh secret set DOTENV -b"$(cat .env)"
```

### 評価上の注意

* Secrets `DOTENV` を登録せずに提出した場合、自動採点ができません
  * 厳密には自動採点が動きますが、ほぼ確実に失敗します
* 遅れて`DOTENV`を登録した場合、 **コードを微妙に変えて再提出** しないと自動採点が動きません
  * Actionsページにある `Re-Run` を使ってもClassroom側には**反映されない**模様です