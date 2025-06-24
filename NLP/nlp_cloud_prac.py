import nlpcloud
client = nlpcloud.Client("mixtral-8x7b", "4eC39HqLyjWDarjtT1zdp7dc" ,gpu=True)
text = """CHK 5000 tbl_num 435/12 2 23 Mar' 2024 13:00:00"""
# Call the generation method
generation = client.generation(
    text,
    max_length=500,
    end_sequence="\n###",
    remove_end_sequence=True,
    remove_input=True
)
# Print the generated text
print(generation["generated_text"])