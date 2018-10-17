# Print the length of the even words in the sentence provided.

st = 'Print every word in this sentence that has an even number of letters'
print(f'{st} \n')

for i in st.split():
    length = [x for x in i]
    count = len(length)
    if count%2==0:
        print(f"{i:>10.10}: has {len(i)} letters")

# A different simpler way of doing it
print('\n')

for word in st.split():
    if len(word)%2==0:
        print(f"{word:>10.10}: has {len(word)} letters")
