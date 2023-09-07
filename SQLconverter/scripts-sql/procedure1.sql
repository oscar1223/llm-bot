CREATE PROCEDURE dbo.proc_Paging_TempTable
(
@Page int,
@RecsPerPage int
)
AS

-- The number of rows affected by the different commands
-- does not interest the application, so turn NOCOUNT ON
SET NOCOUNT ON

-- Determine the first record and last record
DECLARE @FirstRec int, @LastRec int

SELECT @FirstRec = (@Page - 1) * @RecsPerPage
SELECT @LastRec = (@Page * @RecsPerPage + 1)

-- Create a temporary table
CREATE TABLE #TempItems
(RowNum int IDENTITY PRIMARY KEY,
Title nvarchar(100),
Publisher nvarchar(50),
AuthorNames nvarchar(200),
LanguageName nvarchar(20),
FirstLine nvarchar(150),
CreationDate smalldatetime,
PublishingDate smalldatetime,
Popularity int)

-- Insert the rows into the temp table
-- We query @LatRec + 1, to find out if there are more records
INSERT INTO #TempItems (Title, Publisher, AuthorNames, LanguageName,
FirstLine, CreationDate, PublishingDate, Popularity)
SELECT TOP (@LastRec-1)
s.Title, m.Publisher, s.AuthorNames, l.LanguageName,
m.FirstLine, m.CreationDate, m.PublishingDate, m.Popularity
FROM dbo.Articles m
INNER JOIN dbo.ArticlesContent s
ON s.ArticleID = m.ID
LEFT OUTER JOIN dbo.Languages l
ON l.ID = m.LanguageID
ORDER BY m.Popularity desc

-- Return the set of paged records
SELECT *
FROM #TempItems
WHERE RowNum > @FirstRec
AND RowNum < @LastRec

-- Drop the temp table
DROP TABLE #TempItems

-- Turn NOCOUNT back OFF
SET NOCOUNT OFF
GO