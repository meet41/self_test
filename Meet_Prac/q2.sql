-- 1. Find each author's total book-revenue (sum of prices of books that have been LOANED AND RETURNED). Show author name and total.
select authors.name, sum(b.price) from authors INNER JOIN books b ON
 authors.id = b.author_id where b.id IN (SELECT book_id from loans l inner join books b1 ON
                                       l.book_id = b1.id where (loan_date and return_date) is not null GROUP by l.book_id) GROUP by authors.name;
-- 2. Find members with currently active loans (return_date IS NULL), along with the count of their active loans.
 SELECT m.name, count(l.book_id) as current_active from members m inner join loans l ON
 m.id = l.member_id where l.return_date is NULL GROUP by l.book_id, m.name;
-- 3. For each genre, find the most expensive book using a window function. Show genre, title, price.
select genre, title, price from books where price IN (SELECT max(price) over(PARTITION BY genre ORDER BY price DESC) from books);