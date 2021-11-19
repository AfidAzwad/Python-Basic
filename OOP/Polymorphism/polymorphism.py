# poly = many
# morph = form

class Tree:
    def tree_type(self):
        print("There_are_many_types_of_trees.")
    def grass(self):
         print("Most of the grasses have no_category.")

class herbs(Tree):
  def tree_type(self):
   print("herbs are also one form of tree and plant.")

class root(Tree):
  def tree_type(self):
    print("root don’t lie in any tree category.")

tree = Tree()
rt = root()
herb = herbs()

tree.tree_type()

rt.grass()
rt.tree_type()

herb.tree_type()
herb.tree_type()
herb.grass()