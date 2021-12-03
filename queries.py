# 1.
SELECT COUNT(*)
FROM Books
WHERE title = 'A' AJD publisher = 'B' AND branchID IN (
    SELECT branchID
    FROM Branches
    WHERE address = 'C'
)

# 2.
SELECT COUNT(DISTINCT branchID)
FROM Books
WHERE title = 'A'


# 3.
SELECT Borrowers.firstName, Borrowers.lastName, Branches.name
FROM Books
INNER JOIN LentBooks ON Books.bookID = LentBooks.bookID
INNER JOIN Borrowers ON LentBooks.borrowerID = Borrowers.borrowerID
INNER JOIN Branches ON Books.branchID = Branches.branchID
WHERE Books.title = 'A'

# 4.
SELECT Books.title, Borrowers.firstName, Borrowers.lastName, Borrowers.address
FROM LentBooks
INNER JOIN Books ON LentBooks.bookID = Books.bookID
INNER JOIN Borrowers ON LentBooks.borrowerID = Borrowers.borrowerID
WHERE LentBooks.dueDate = getToday() AND branchID = 'A'



# 5.
SELECT COUNT(DISTINCT Branches.branchID), Branches.name
FROM Branches
INNER JOIN Books ON Branches.branchID = Books.branchID
WHERE bookID IN (
    SELECT bookID
    FROM LentBooks
)