# Task 1: Keyword Highlighter
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "This was a poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."]

keywords = ["good", "excellent", "bad", "poor", "average"]

def highlight_keywords(reviews, keywords):
    highlighted_reviews = []
    for review in reviews:
        for keyword in keywords:
            review = review.replace(keyword, keyword.upper())
        highlighted_reviews.append(review)
    return highlighted_reviews

highlighted_reviews = highlight_keywords(reviews, keywords)
for review in highlighted_reviews:
    print(review)

# Task 2: Sentiment Tally
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def sentiment_tally(reviews, positive_words, negative_words):
    tally_results = []
    for review in reviews:
        positive_count = sum(word in review for word in positive_words)
        negative_count = sum(word in review for word in negative_words)
        tally_results.append((positive_count, negative_count))
    return tally_results

tally_results = sentiment_tally(reviews, positive_words, negative_words)
for i, (pos_count, neg_count) in enumerate(tally_results):
    print(f"Review {i+1}: {pos_count} positive words, {neg_count} negative words")

# Task 3: Review Summary
def create_summary(review):
    if len(review) <= 30:
        return review
    if review[29].isspace():
        return review[:30] + "..."
    else:
        last_space_index = review[:30].rfind(' ')
        return review[:last_space_index] + "..."

summaries = [create_summary(review) for review in reviews]
for summary in summaries:
    print(summary)
