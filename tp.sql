//-------------------------------------------------------------
// Problem Statement 7 (MapReduce)
// Book Collection: (title, author_name, borrowed_status, price)
//-------------------------------------------------------------

// 1️⃣ Create / Use Database
use libraryDB;

// 2️⃣ Create Collection and Insert Sample Documents
db.bookCollection.insertMany([
  { title: "Early India", author_name: "Romila Thapar", borrowed_status: true,  price: 1200 },
  { title: "Verity", author_name: "Colleen Hoover", borrowed_status: false, price: 250 },
  { title: "Nelson Mandela", author_name: "Hovely Reads", borrowed_status: true, price: 900 },
  { title: "Everyday Gita", author_name: "Sunita Pant", borrowed_status: false, price: 1500 },
  { title: "Book A", author_name: "Colleen Hoover", borrowed_status: true,  price: 400 }
]);

//-------------------------------------------------------------
// 3️⃣ MAP REDUCE 1 → Author-wise list of all books
//-------------------------------------------------------------
var map1 = function() {
    emit(this.author_name, this.title);
};

var reduce1 = function(key, values) {
    return values;
};

db.bookCollection.mapReduce(
    map1,
    reduce1,
    { out: "author_books" }
);

print("\n--- Author-wise list of all books ---");
db.author_books.find().forEach(printjson);

//-------------------------------------------------------------
// 4️⃣ MAP REDUCE 2 → Author-wise list of books with Borrowed_status = true
//-------------------------------------------------------------
var map2 = function() {
    if (this.borrowed_status === true)
        emit(this.author_name, this.title);
};

var reduce2 = function(key, values) {
    return values;
};

db.bookCollection.mapReduce(
    map2,
    reduce2,
    { out: "borrowed_books" }
);

print("\n--- Author-wise list of borrowed books ---");
db.borrowed_books.find().forEach(printjson);

//-------------------------------------------------------------
// 5️⃣ MAP REDUCE 3 → Author-wise list of books with price > 300
//-------------------------------------------------------------
var map3 = function() {
    if (this.price > 300)
        emit(this.author_name, this.title);
};

var reduce3 = function(key, values) {
    return values;
};

db.bookCollection.mapReduce(
    map3,
    reduce3,
    { out: "pricey_books" }
);

print("\n--- Author-wise list of books having price > 300 ---");
db.pricey_books.find().forEach(printjson);
