resource "aws_iam_user" "this"{
    for_each = toset(var.user)
    name = each.value
}