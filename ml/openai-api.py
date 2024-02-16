from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
cors = CORS(app)


# Set your OpenAI API key
openai.api_key = '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'

@app.route('/',methods=['GET'])
def hello():
    return jsonify({"ee":'hello'})

'''@app.route('/financial-advisor', methods=['POST'])
def financial_advisor():
    try:
        # Get the user's question from the JSON body of the POST request
        user_question = request.json.get('question')

        # Modify the system prompt accordingly
        system_prompt = "As a financial expert, answer the following question:\n\n"

        # Combine the system prompt and user question
        prompt = f"{system_prompt}{user_question}"

        # Call OpenAI API to generate a financial-based response
        response = openai.Completion.create(
            model="gpt-3.5-turbo-0125",  # Use the GPT-3.5-turbo model
            prompt=prompt,
            temperature=0.7,
            max_tokens=150,
            n=1,
            stop=None
        )

        # Extract the generated answer from the OpenAI response
        generated_answer = response['choices'][0]['text'].strip()

        # Prepare the response
        api_response = {'answer': generated_answer}

        return jsonify(api_response), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500'''
@app.route('/financial-advisor', methods=['POST'])
def financial_advisor():
    try:
        user_question = request.json.get('question')

        # Call OpenAI Chat API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "system", "content": "You are a knowledgeable financial advisor."},
                {"role": "user", "content": user_question}
            ]
        )

        # Extract the generated answer
        generated_answer = response['choices'][0]['message']['content']

        # Prepare the response
        api_response = {'answer': generated_answer}

        return jsonify(api_response), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)