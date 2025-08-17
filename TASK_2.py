TTW=input("Enter text to write to the file: ")
with open("output.txt","w") as f:
    f.write(TTW+"\n")
print("Data successfully written to output.txt.")
TTA=input("Enter additional text to append: ")
with open("output.txt","a") as f:
    f.write(TTA+"\n")
print('Data Sucessfully appended.')
print("\nFinal content of output.txt:")
with open("output.txt", "r") as f:
    print(f.read())
