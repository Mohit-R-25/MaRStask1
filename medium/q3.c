#include <stdio.h>
#include <string.h>

int main() {
    char input[100], output[100];
    int shift=0;
    printf("Enter the encrypted message: ");
    scanf("%s", input);

    int len = strlen(input);

    for(int i = 0; i < len; i++) {
        char ch = input[i];

        //Convert lowercase to uppercase:
        if(ch >= 'a' && ch <= 'z') {
            ch = ch - 32;
        }
        shift = i + 1;  // shift amount increases by position(1-based)

        // reverse the shift:
        ch = ch - shift;

        // wrap around if inputted character is before 'A'
        if(ch < 'A') {
            ch = ch + 26;
        }

        output[i] = ch;
    }

    output[len] = '\0';  //null terminate the string

    printf("Decoded message: %s\n", output);

    return 0;
}
