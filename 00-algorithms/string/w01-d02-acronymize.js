/* 
  Acronyms

  Create a function that, given a string, returns the string’s acronym 
  (first letter of each word capitalized). 

  Do it with .split first if you need to, then try to do it without
*/

const str1 = "object oriented programming";
const array= str1.split('');
console.log(array[0]);
console.log(array[1]);
console.log(array[2]);

const expected1 = "OOP";

The 4 pillars of OOP
 const str2 = "abstraction polymorphism inheritance encapsulation";
 const chars= str1.split('')
 console.log(chars);
 const expected2 = "APIE";

 const str3 = "software development life cycle";
const expected3 = "SDLC";

//  Bonus: ignore extra spaces
const str4 = "  global   information tracker    ";
const expected4 = "GIT";

 function acronymize(str) {
 var arr=str.split(" ")   
 
 console.log(arr);


 }