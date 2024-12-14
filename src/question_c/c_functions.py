#write functions here, don't add input('') statements here!

# The question specified that the output of the function below should be separate parameters instead of a list or string
# Took me a very long time to get working
# The commented code below was an earlier attempt to output as instructed

# def get_most_likely_ancestor_consensus(dna_string1, dna_string2):
#     indexer = -1
#     for i in range(len(dna_string1)):
#         if dna_string1[i:i+4] == dna_string2:
#             current_position = i
#             indexer += 1
#             position_name = "position" + str(indexer)
#             exec(f"{position_name} = {current_position}")
#             return_list += f"{position_name}, "
    # execute_string = "indexer, " + return_list
    # execute_string = execute_string[:-2]
    # return exec(f"{execute_string}")

def get_most_likely_ancestor_consensus(dna_string1, dna_string2):
    for pos in range(len(dna_string1)):
        if dna_string1[pos:pos+4] == dna_string2:
            current_position = pos + 1
            yield current_position

def get_amt_of_positions(dna_string1, dna_string2):
    counter = 0
    for pos in range(len(dna_string1)):
        if dna_string1[pos:pos+4] == dna_string2:
            counter += 1
    return counter

def verify_initial_strand(strand : str):
    strand_length = len(strand)
    if strand_length < 8 or strand_length > 16:
        return False
    else:
        return True
    
def verify_second_strand(strand : str):
    strand_length = len(strand)
    if strand_length == 4:
        return True
    else:
        return False