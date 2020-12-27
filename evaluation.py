import json
from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('paraphrase-distilroberta-base-v1')
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
from nltk.corpus import stopwords  
from nltk.tokenize import word_tokenize  
from nltk.stem import WordNetLemmatizer 
import re
import requests
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english')) 


def cosine_similarity_preprocessor(answer):
    answer=answer.lower()
    answer= re.sub(r'[^\w\s]', ' ', answer)
    word_tokens = word_tokenize(answer)  
    filtered_sentence = []  
    for w in word_tokens:  
        if w not in stop_words:
            w=lemmatizer.lemmatize(w)
            filtered_sentence.append(w) 
    filtered_ans=listToStr = ' '.join([str(elem) for elem in filtered_sentence])
    return filtered_ans

def cosine_similarity(model_answer,answer):
  return 0
  model_answer=cosine_similarity_preprocessor(model_answer)
  answer=cosine_similarity_preprocessor(answer)
  embeddings1 = model.encode(model_answer, convert_to_tensor=True)

  embeddings2 = model.encode(answer, convert_to_tensor=True)
  cosine_scores = util.pytorch_cos_sim(embeddings1, embeddings2)
  return cosine_scores

def check_grammar(answer):
  req = requests.get("https://api.textgears.com/check.php?text=" + answer + "&key=JmcxHCCPZ7jfXLF6")
  no_of_errors = len(req.json()['errors'])
  if no_of_errors > 5 :
        return 0
  else:
        return 1
    
def results(marks,model_ans,user_ans):
    
    cosine_score=cosine_similarity(model_ans,user_ans)
    grammar=check_grammar(user_ans)
    marks1=int(int(cosine_score)*int(marks))
    print(marks1)
    print(grammar)

    
    return_data = [
        {
            'marks': '5',
            'marks out of': '5',
            'keywords': 'Milk, Cheese, Pizza, Fruit, Tylenol', 
            'spellings': 'oo'
        }
    ]
    return json.dumps(return_data)