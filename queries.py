# 1
SELECT COUNT(*)
FROM books
WHERE title = 'A' AND publisher = 'B' AND branchID IN (
    SELECT branchID
    FROM branches
    WHERE address = 'C'
);

# 2
SELECT COUNT(branchID)
FROM Books
WHERE title = 'A'
GROUP BY branchID;

# 3
SELECT borrowers.firstName, borrowers.lastName, branches.name
FROM books
INNER JOIN lentBooks ON books.bookID = lentBooks.bookID
INNER JOIN borrowers ON lentBooks.borrowerID = borrowers.borrowerID
INNER JOIN branches ON books.branchID = branches.branchID
WHERE books.title = 'A';

# 4
SELECT books.title, borrowers.firstName, borrowers.lastName, borrowers.address
FROM lentBooks
INNER JOIN books ON lentBooks.bookID = books.bookID
INNER JOIN borrowers ON lentBooks.borrowerID = borrowers.borrowerID
WHERE lentBooks.dueDate = getToday() AND branchID = 'A';

# 5
SELECT branches.name, COUNT(bookID)
FROM branches
INNER JOIN books ON branches.branchID = books.branchID
WHERE bookID IN (
    SELECT lentBooks.bookID
    FROM lentBooks
    )
GROUP BY branches.branchID;