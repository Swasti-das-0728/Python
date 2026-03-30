from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import graphviz

# Sample data
X = [[0, 0], [1, 1]]
y = [0, 1]

model = DecisionTreeClassifier()
model.fit(X, y)

# Export tree
dot_data = tree.export_graphviz(model, out_file=None)

graph = graphviz.Source(dot_data)
graph.render("decision_tree", view=True)