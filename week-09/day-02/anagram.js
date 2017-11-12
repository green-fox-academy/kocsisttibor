function checkAnagram(string1, string2) {
    let arr1 = string1.split('').sort();
    let arr2 = string2.split('').sort();
    if (arr1.length === arr2.length) {
        for (let i = 0; i < arr1.length; i++) {
            if (arr1[i] !== arr2[i]) {
                return false;
            }
        }
        return true;
    } else {
        return false;
    }
}

module.exports = checkAnagram;