package Utils;

public class NodeBuilder {
    private int value;
    private Node left;
    private Node right;

    public NodeBuilder() {
    }

    public NodeBuilder withValue(int value) {
        this.setValue(value);
        return this;
    }

    public NodeBuilder withLeft(Node left) {
        this.setLeft(left);
        return this;
    }

    public NodeBuilder withRight(Node right) {
        this.setRight(right);
        return this;
    }

    public NodeBuilder withNodes(Node left, Node right) {
        this.setLeft(left);
        this.setRight(right);
        return this;
    }

    public Node build() {
        return new Node(this.getValue(), this.getLeft(), this.getRight());
    }

    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public Node getLeft() {
        return left;
    }

    public void setLeft(Node left) {
        this.left = left;
    }

    public Node getRight() {
        return right;
    }

    public void setRight(Node right) {
        this.right = right;
    }
}
