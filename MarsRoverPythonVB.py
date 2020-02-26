
##  =======================================================================
##                       File Variables Treatment
##  =======================================================================

import os       
# For remove output's file if exists


#Get the lines of the input file and save them in their respective variables

#Check the existence of the output file and delete it

def GetVariables():

        with open ("input.txt", "r") as FileContent:

                if os.path.exists("output.txt"):
                        os.remove("output.txt")

                Content=FileContent.readlines()

                i=0
                ListPosition=[]
                ListInstruction=[]
                
        for i,x in enumerate(Content):

                if i==0:
                        GridLenth=x.replace('\n', '')
                        
                elif i%2==0:
                        
                        Aux=Content[i].replace('\n', '')
                        ListInstruction.append(Aux)
                        
                else:
                        Aux=Content[i].replace('\n', '')
                        ListPosition.append(Aux)
                        

        FileContent.close()
        
        return( GridLenth , ListPosition , ListInstruction)



#Get the size of the plateau, given by the file and delete the spaces

def GetGridVariables(GridLength):

        GridLength = GridLength.split()
        Height = GridLength[0]
        Width = GridLength[1]

        if Height != Width:
                raise Exception('Height: {} should be equal to Width: {} .'.format( Height , Width ))
        else:
                return(Height,Width)


#Write the result in the output file
def WriteFile(X,Y,C):

        X = str(X)
        Y = str(Y)

        Output = X+' '+Y+' '+C

        with open('output.txt', 'a+') as WriteFile:
                WriteFile.write(Output)
                WriteFile.write("\n")
                WriteFile.close

        return 0



##  =======================================================================
##                       List Treatment
##  =======================================================================


#Remove the first item in a given list
def DeleteListElement(List):

        if len(List) > 1 :

                List = List.pop(0)
                
                return(List)
        
        elif len(List) == 1:

                List = List[0]
                
                return(List)

        else:
                return 0

##  =======================================================================
##                           Position Functions
##  =======================================================================

        
#Get the coordinates and remove the spaces
def GetCoordinates(ListPosition):

        if len(ListPosition ) > 1:

                Aux=ListPosition[0]

                Position=Aux.split(" ")

                X=Position[0]
                Y=Position[1]
                C=Position[2]

                C = C.upper()

                if C != "N" and C != "S" and C != "E" and C != "W":

                        raise Exception('Coordinates have wront format: {}'.format(C))


                else:
                
                        ListPosition= ListPosition.pop(0)
                
                        return(X,Y,C)

        elif len(ListPosition ) == 1:


                StringPosition = ListPosition[0]

                Position=StringPosition.split(" ")

                X=Position[0]
                
                Y=Position[1]
                
                C=Position[2]
                

                return(X,Y,C)

        else:
                print("Problem getting Coordinates")

##  =======================================================================            
##                           Instruction Functions
##  =======================================================================

                
#Get the first value in a list and then delete that value in the list
def GetInstructionHead(ListInstruction):


        if len(ListInstruction) > 1 :

                HeadInstruction = ListInstruction[0]
                ListInstruction = ListInstruction.pop(0)

                return(HeadInstruction)

        elif len(ListInstruction) == 1:

                HeadInstruction = ListInstruction[0]

                return(HeadInstruction)

        else:
                print("Problem getting InstructionHead")


                
#Get the current instruction and the following instructions for future treatment
def GetCurrentInstruction(ListInstructionHead):



        if len(ListInstructionHead) >= 1 :
                
                CurrentInstruction = ListInstructionHead[0]
                Len = len(ListInstructionHead)
                NextInstructions = ListInstructionHead[1:Len]
                        
                return (CurrentInstruction,NextInstructions)

        else:
                
                NoCurrentInstruction = True
                WithOutInstructions = True

                return (NoCurrentInstruction,WithOutInstructions)



#Given the instructions move the Rover according to these
def TurnRover(X , Y , C , CurrentInstruction):

        X = int(X)
        Y = int(Y)

        C = C.upper()

        CurrentInstruction = CurrentInstruction.upper()
        
        try:
                if CurrentInstruction == "L":

                        if C == "N":
                                C = "W"
                                return(X,Y,C)
                        
                        elif C == "E":
                                C = "N"
                                
                                return(X,Y,C)
                        
                        elif C == "S":
                                C = "E"
                                return(X,Y,C)
                        
                        elif C == "W":
                                C = "S"
                                return(X,Y,C)
                        
                        else:
                                print("Wrong Format")

                elif CurrentInstruction == "R":
                        
                        if C == "N":
                                
                                C = "E"
                                
                                return(X,Y,C)
                        
                        elif C == "E":
                                
                                C = "S"
                                
                                return(X,Y,C)
                        
                        elif C=="S":
                                
                                C="W"
                                
                                return(X,Y,C)
                        
                        elif C == "W":
                                
                                C = "N"
                                
                                return(X,Y,C)
                        
                        else:
                        
                                print("Wrong Format")
                        
                        return(X,Y,C)

                elif CurrentInstruction == "M":
                        
                        if C == "N":
                                Y = Y+1
                                Y = str(Y)
                                
                                return(X,Y,C)
                        
                        elif C == "E":
                                
                                X = X+1
                                X = str(X)
                                
                                return(X,Y,C)
                        
                        elif C == "S":
                                
                                Y = Y-1
                                Y = str(Y)
                                
                                return(X,Y,C)
                        
                        elif C == "W":
                                
                                X = X-1
                                X = str(X)
                                
                                return(X,Y,C)
                        
                        else:
                                print("Wrong Format")

                        return(X,Y,C)

        except ValueError:

                print("Wrong Format")



##  =======================================================================            
##                           Plateau Object
##  =======================================================================

def PlateauAreaLimit (Height,X , Y):

        
        Height = int(Height)
        X = int(X)
        Y = int(Y)

        if (X >= 0 and X <= Height) and (Y >= 0 and Y <= Height):

                return 0

        else:
               raise Exception('X: {} and Y: {} should be into the Plateau: .'.format( X , Y )) 

        


##  =======================================================================            
##                           Main Function
##  =======================================================================



def main():

##             The previously performed functions are invoked
        
        
        GridLenth,ListPosition,ListInstruction = GetVariables()
        
        Height,Width = GetGridVariables(GridLenth)

        InstructionHead = GetInstructionHead(ListInstruction)

        LenList = len(ListPosition)

        #Repeats as many Rovers are found

        for i in range(0, LenList):              
               
                X,Y,C = GetCoordinates( ListPosition )

                PlateauAreaLimit( Height , X , Y )

                CurrentInstruction , NextInstructions = GetCurrentInstruction(InstructionHead)

                #Repeated for every instruction found
                
                for i in InstructionHead:
                        
                        
                        X,Y,C=TurnRover(X,Y,C,CurrentInstruction)

                        PlateauAreaLimit( Height , X , Y )

                        CurrentInstruction , NextInstructions = GetCurrentInstruction(NextInstructions)


                #The first item in the list is removed for the next iteration
                InstructionHead =  DeleteListElement(ListInstruction)

                
                #The current instruction and the next instructions are updated
                CurrentInstruction , NextInstructions = GetCurrentInstruction(InstructionHead)

                
                #It is written to file for each rover
                WriteFile(X , Y , C)
                                
        
if __name__== "__main__":
        main()


