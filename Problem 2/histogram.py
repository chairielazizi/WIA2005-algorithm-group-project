import wordcounts
import plotly, plotly.graph_objects as go

#plot histogram of word frequency
for s in wordcounts.wordListNoStopWords:
    x = [a for a in wordcounts.wordListNoStopWords]
    y = [wordcounts.wordListNoStopWords.count(p) for p in wordcounts.wordListNoStopWords]
fig = go.Figure()
fig.add_trace(go.Histogram(histfunc="count", y=y, x=x, name="count"))
fig.update_layout(
    title="Word Frequency",
    xaxis_title="Word",
    yaxis_title="Count",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="RebeccaPurple"
    )
)
fig.show()

# plot histogram of positive word frequency
for s in wordcounts.positiveWordList:
    x = [a for a in wordcounts.positiveWordList]
    y = [wordcounts.positiveWordList.count(p) for p in wordcounts.positiveWordList]
fig = go.Figure()
fig.add_trace(go.Histogram(histfunc="count", y=y, x=x, name="count"))
fig.update_layout(
    title="Positive Word Frequency",
    xaxis_title="Word",
    yaxis_title="Count",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="RebeccaPurple"
    )
)
fig.show()

# plot histogram of negative word frequency
for s in wordcounts.negativeWordList:
    x = [a for a in wordcounts.negativeWordList]
    y = [wordcounts.negativeWordList.count(p) for p in wordcounts.negativeWordList]
fig = go.Figure()
fig.add_trace(go.Histogram(histfunc="count", y=y, x=x, name="count"))
fig.update_layout(
    title="Negative Word Frequency",
    xaxis_title="Word",
    yaxis_title="Count",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="RebeccaPurple"
    )
)
fig.show()