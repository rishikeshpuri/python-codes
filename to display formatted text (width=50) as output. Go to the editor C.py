import textwrap
sample_text='''
Python is a widely used high-level, general-purpose, interpreted,
  dynamic programming language. Its design philosophy emphasizes
  code readability, and its syntax allows programmers to express
  concepts in fewer lines of code than possible in languages such
  as C++ or Java.'''
print()
print(textwrap.fill(sample_text,width=50))
print()
text_without_Indentation = textwrap.dedent(sample_text)
print()
print(text_without_Indentation )
print()
wrapped = textwrap.fill(text_without_Indentation, width=50)
final_result = textwrap.indent(wrapped, '> ')
print()
print(final_result)
print()