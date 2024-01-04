import os
from langchain.llms import CTransformers 
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferMemory

model_id = 'TheBloke/Mistral-7B-Instruct-v0.1-GGUF'
# model_id = 'TheBloke/Mistral-7B-codealpaca-lora-GGUF'
os.environ['XDG_CACHE_HOME']= './model'
config  ={'temperature':1.00,'context_length':5000,}
#shjfgshjgfhsgfhsgfhsgjdgfjhsdggfds
llm = CTransformers(model = model_id, model_type='mistral', config=config, callbacks= [StreamingStdOutCallbackHandler()])

print(llm("Write a poem on guitar."))
