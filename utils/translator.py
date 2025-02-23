from google import genai

DEFAULT_PROMPT = """# 指示
日本語で書かれた人文科学分野の博士論文のメモを、アカデミックライティングの作法に沿って英語に翻訳してください。

# 翻訳の際の注意点
- 文法、語彙、句読点、スペルなど、英語のアカデミックライティングのルールに厳密に従うこと。受動態をなるべく使わないこと。
- 専門用語は、当該分野で適切な英語の用語を使用すること。必要であれば、翻訳ツールや辞書を参照すること。
- 文体は、客観的で論理的な表現を心がけること。
- 翻訳された文章は、博士論文の執筆に使用できる品質であることを期待する。
""" 

# プロンプト
prompt = """
{message}

翻訳するテキスト:
{input}

期待される出力：
(翻訳後のテキストのみを記載する)
"""


class Translator:
    def __init__(self, api_key, model_name):
        self.client = genai.Client(
            api_key=api_key
        )
        self.model_name = model_name

    def translate(self, message, input):
        response = self.client.models.generate_content(
            model = self.model_name,
            contents=[prompt.format(message=message, input=input)]
        )
        return response
    
