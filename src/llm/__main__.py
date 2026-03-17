# write main function to run the application
from email.mime import text

from llm.gpt.tensors import TensorPlayGround
from llm.gpt.tokenizers import SimpleTokenizerV2

def main():
    print("Writing, own llm from scratch!")
    tensorPlayGround = TensorPlayGround([1, 2, 3])
    tensorPlayGround.print_torch_info()

    tokenizer = SimpleTokenizerV2(vocab)

    text1 = "Hello, do you like tea?"
    text2 = "In the sunlit terraces of the palace."

    text = " <|endoftext|> ".join((text1, text2))

    print(text)

if __name__ == "__main__":
    main()