var parent = document.querySelector('div');
const kids = [{"pet_name":"Wattled crane","owner":"Bryant"},
    {"pet_name":"Devil, tasmanian","owner":"Alejandro"},
    {"pet_name":"Mynah, common","owner":"Nelie"},
    {"pet_name":"Dolphin, common","owner":"Mariele"},
    {"pet_name":"Gray duiker","owner":"Maddalena"},
    {"pet_name":"Crab (unidentified)","owner":"Lucine"},
    {"pet_name":"Ant (unidentified)","owner":"Lorianna"},
    {"pet_name":"Bison, american","owner":"Tommie"},
    {"pet_name":"Yellow mongoose","owner":"Vivyan"},
    {"pet_name":"Carpet snake","owner":"Veda"},
    {"pet_name":"Lesser mouse lemur","owner":"Isidor"}]

kids.forEach(function(e, i) {
    var child = document.createElement('article');
    parent.appendChild(child);
    var h3 = document.createElement('h3');
    child.appendChild(h3);
    h3.textContent = kids[i].owner;
    var p = document.createElement('p');
    child.appendChild(p);
    p.textContent = kids[i].pet_name;
})
