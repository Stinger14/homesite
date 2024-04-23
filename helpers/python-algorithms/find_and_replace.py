def findAndReplace(text, oldText, newText):
    """
    Find and replace a substring in a string
    """
    # Initialize the result:
    result = ''
    # Initialize the index:
    index = 0
    # Iterate through the text:
    while index < len(text):
        # If the substring is found:
        if text[index:index+len(oldText)] == oldText:
            # Add the new text to the result:
            result += newText
            # Increment the index by the length of the old text:
            index += len(oldText)
        else:
            # Add the current character to the result:
            result += text[index]
            # Increment the index:
            index += 1
    # Return the result:
    return result
    