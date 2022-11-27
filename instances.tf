resource "aws_vpc" "this" {
    cidr_block = var.vpc_cidr
    enable_dns_support = "true"
    enable_dns_hostnames = "true"
    tags = var.vpc_tags
}

resource "aws_subnet" "this" {
    vpc_id = aws_vpc.this.id
    cidr_block = var.subnet_cidr
    tags = var.subnet_tags
    availability_zone = var.availability_zone
}

module "instance" {
    source = "./instance_module"

    for_each = {for instance in var.instances : instance.name => instance}
    name = each.value.name
    type = "t2.${each.value.size}"
    security_group = each.value.security_group
    subnet_id = aws_subnet.this.id
    vpc_id = aws_vpc.this.id
    ingress_from_port = var.ingress_from_port
    ingress_to_port = var.ingress_to_port
    ingress_protocol = var.ingress_protocol
    egress_from_port = var.egress_from_port
    egress_to_port = var.egress_to_port
    egress_cidr_block = var.egress_cidr_block
    AMI = var.AMI
    availability_zone = var.availability_zone
    egress_protocol = var.egress_protocol
    cidr_block = var.cidr_block
    route_table_cidr_block = var.route_table_cidr_block
    route_table_gateway_id = var.route_table_gateway_id
    route_table_tags = var.route_table_tags
    AWS_REGION = var.AWS_REGION

}