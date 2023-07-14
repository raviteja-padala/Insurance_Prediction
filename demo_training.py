## training Pipeline

from Insurance.pipeline.training_pipeline import start_training_pipeline

if __name__=="__main__":
    try:
        
        output = start_training_pipeline()
        print("output=",output)
        
    except Exception as e:
        print(e) 