## Batch Prediction


from Insurance.pipeline.batch_prediction import start_batch_prediction

file_path = r"C:\Users\Lenovo\Desktop\Insurance_Prediction\insurance.csv"

if __name__=="__main__":
    try:
        output = start_batch_prediction(input_file_path=file_path)
        
        print("Batch prediction done, csv generated")
        #output = start_training_pipeline()
        #print(output)
        
    except Exception as e:
        print(e)