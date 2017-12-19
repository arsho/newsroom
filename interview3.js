// Question
// We have a string and we want to capitalize the words
// which start with a vowel.

// It would be great if you can wrap it up within 5 minutes

function i_am_making_wordsStartsWithVowel_bolder() {
    var str = "what ever i am writing here or have wrote this is all my (first) imagination (second) creation, words with all 5 vowels, which i got from dictionary one by one page, i think all will enjoy and increase knowledge thats my education.";
    var s = '';
    var spaceFlag = 0;
    var capitalFlag = 0;
    for (var i = 0; i < str.length; i++) {
        if (spaceFlag == 1 || i == 0) {
            if (str[i].toLowerCase() == 'a' ||
                str[i].toLowerCase() == 'e' ||
                str[i].toLowerCase() == 'i' ||
                str[i].toLowerCase() == 'o' ||
                str[i].toLowerCase() == 'u') {
                capitalFlag = 1;
            }
        }
        if (str[i] == " " && spaceFlag == 0) {
            spaceFlag = 1;
            capitalFlag = 0;
        }
        else if (str[i] != " ") {
            spaceFlag = 0;
        }
        if (capitalFlag == 1) {
            s += str[i].toUpperCase();
        }

        else {
            s += str[i];
        }

    }
    return s;
}

console.log(i_am_making_wordsStartsWithVowel_bolder());