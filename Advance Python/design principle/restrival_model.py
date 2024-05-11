from abc import ABC,abstractmethod
class retrival_model(ABC):
    @abstractmethod
    def restrive_information(self,query):
        pass 
    
    
    
class vector_db_pattern(ABC):
    def connection(self):
        print("connecting to the vector db")
        
    
    @abstractmethod
    def data_retrieval(self,query):
        pass
    
    @abstractmethod
    def meta_data_info(self,query):
        pass
    
    @abstractmethod
    def updating_record(self,doc):
        pass
    
    @abstractmethod
    def updating_many_records(self,docs):
        pass
    
# RAG model pipeline


class llm_model_pattern(ABC):
    @abstractmethod
    def stream(self):
        pass
    
    @abstractmethod
    def cost_details(self):
        pass
    
class rag_model_response:
    def __init__(self,llm_model_obj):
        self.llm_model_obj = llm_model_obj
    
    def streaming(self):
        return self.llm_model_obj.stream()
    
    def cost_estimate(self):
        self.llm_model_obj.cost_details()    
        
        

def connection():
    ind = 10
    while ind>=0:
        ind-=1
        yield "data is "+ f" {ind}"

class azure_open_ai(llm_model_pattern):
    def __init__(self,model_name):
        self.model_deployment = connection
        
    
    def stream(self):
        return self.model_deployment()
    def cost_details(self):
        
        return "some_random_cost for now"