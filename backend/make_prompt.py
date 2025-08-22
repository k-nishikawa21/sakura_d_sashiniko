def make_prompt(input_text):
    prompt = f"""
# 命令書
あなたは高度な技術を持つチームリーダーです。 以下の指示とレビューコメント案に基づき、中級者の部下が指導内容を深く理解できるような、レビューコメントを作成してください。

# 入力文
{input_text}

# 回答の条件
- 解答は，「お疲れ様です」から始めてください。
- レビュー対象の文は、部下が書いた文章です。
- 上司の指摘の核となる意図を1～2文で簡潔にまとめること。
- 部下に向けて送るレビューコメントのみを出力すること。
- 部下のことは「あなた」と呼ぶこと。
- 専門用語は適切に使用し、その概念も簡潔に説明すること。

# 思考プロセス
1. レビューコメント案の意図を深く理解する。
2. レビュー対象の文を読んで、指摘内容を全て洗い出す。
3. レビューコメントを作成する。
4. レビューコメントを簡潔にする。


# 回答の例
 # 入力文（例）
 　８/21と8月22日は在宅勤務とさせていただきます
 # レビューコメント案
 　表記ゆれ
 # 出力例
 　お疲れ様です。「８/21」と「8月22日」の表記が異なっています。統一して「8月21日」と「8月22日」としてください。
 　

    """

    return prompt

def make_final_prompt(input_text, media_file=None):
    # with open(media_file, "r", encoding="utf-8") as f:
    #     # 全部読み込む
    #     media_content = f.read()
    media_content = media_file.getvalue().decode("utf-8")
    # プロンプトを作成
    input_text = f"""
# レビュー対象のもの
{input_text}
# 指摘ポイント
{media_content}
"""
    prompt = make_prompt(input_text)
    return prompt