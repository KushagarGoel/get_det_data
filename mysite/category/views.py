from pickle import load

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
from .model import predict
import nltk
import string



from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


f=open('../static/media/keras.txt','r',errors = 'ignore')
raw=f.read().lower()
sent = nltk.sent_tokenize(raw)# converts to list of sentences


sent_tokens = nltk.sent_tokenize(raw)# converts to list of sentences
word_tokens = nltk.word_tokenize(raw)# converts to list of words


lemmer = nltk.stem.WordNetLemmatizer() #WordNet is a semantically-oriented dictionary of English included in NLTK.
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))



def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response


termi = ['bye','exit','quit','thanks','thanku','thank you']
greets = ["hello", "hi", "greetings","hey"]



def get_response(user_response):
    global j
    while(j):
        if(user_response not in termi):
            if(user_response in greets):
                return("I would be glad to help you")
            else:
                resp = response(user_response)
                sent_tokens.remove(user_response)
                return(resp)

        else:
            j = False
            return("It was nice assisting you")

j = True

def home(request):
    return render(request,"category/home.html",{})

def get_bot_response(request):
    userText = request.GET['msg']
    yo = get_response(str(userText))
    return HttpResponse(yo)



def MlModel(request):
    res = predict()
    return JsonResponse(res)


