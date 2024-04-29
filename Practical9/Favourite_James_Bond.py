#define the function
def bond(birthyear):
    #calculate the year of 18 years old
    year=int(birthyear)+18
    #find the James Bond actor in the year
    if 1973<=year<=1986:
        bond='Roger Moore'
    if 1987<=year<=1994:
        bond='Timothy Dalton'
    if 1995<=year<=2005:
        bond='Pierce Brosnan'
    if 2006<=year<=2021:
        bond='Daniel Craig'
    #return the actor's name
    return(bond)
#call the function: input the birth year and print the result
print('You were born in year:')
print(bond(input()))
