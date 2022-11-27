resource "aws_instance" "instance" {
    
    ami = var.AMI
    instance_type = var.type
    

    tags = {
        Name = var.name
    }

    subnet_id = var.subnet_id
    vpc_security_group_ids = [aws_security_group.this.id]
}

resource "aws_security_group" "this" {
    name = var.security_group
    vpc_id = var.vpc_id


    egress {
        from_port = var.egress_from_port
        to_port = var.egress_to_port
        protocol = var.egress_protocol
        cidr_blocks = var.egress_cidr_block
    }

    ingress {
        from_port = var.ingress_from_port
        to_port = var.ingress_to_port
        protocol = var.ingress_protocol
        cidr_blocks = var.cidr_block
    }

    tags = {
        Name = var.security_group
    }
}