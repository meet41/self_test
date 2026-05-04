-- 1. Find each author's total book-revenue (sum of prices of books that have been LOANED AND RETURNED). Show author name and total.
SELECT a.name, SUM(b.price) AS total_revenue
FROM authors a
JOIN books b ON a.id = b.author_id
JOIN loans l ON b.id = l.book_id
WHERE l.return_date IS NOT NULL
GROUP BY a.name;
-- 2. Find members with currently active loans (return_date IS NULL), along with the count of their active loans.
SELECT m.name, COUNT(*) AS active_loans
FROM members m
JOIN loans l ON m.id = l.member_id
WHERE l.return_date IS NULL
GROUP BY m.id, m.name;
-- 3. For each genre, find the most expensive book using a window function. Show genre, title, price.
SELECT genre, title, price
FROM (
    SELECT genre, title, price,
           ROW_NUMBER() OVER (PARTITION BY genre ORDER BY price DESC) AS rn
    FROM books
) t
WHERE rn = 1;