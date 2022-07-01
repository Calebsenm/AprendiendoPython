class Car:
    # #atributes 
    # Make = None
    # Model = None
    # Year = None
    # Color = None

    #constructor
    def __init__(self,make,model,year,color):
        #atributes 
        self.Make = make
        self.Model = model
        self.Year = year
        self.Color = color



    # metodos 
    def drive(self):
        print(f"the {self.Make} is driving")
    
    
    def stop(self):
        print(f"this {self.Make} is stopped") 