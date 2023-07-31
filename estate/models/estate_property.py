from odoo import models, fields
from datetime import date, timedelta


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Real estate property'

    name = fields.Char(required=True)
    active = fields.Boolean('Active', default=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Char(
        readonly=True, default=lambda self: date.today() + timedelta(days=90))
    expected_price = fields.Float(readonly=True)
    selling_price = fields.Float(readonly=True)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Orientation',
        selection=[('North', 'North'), ('South', 'South'),
                   ('East', 'East'), ('West', 'West')],
        help='Orientation is used to separate orientation types'
    )
    state = fields.Selection([
        ('New', 'New'),
        ('Offer Received', 'Offer Received'),
        ('Offer Accepted', 'Offer Accepted'), ('Sold', 'Sold'),  ('Canceled', 'Canceled')], 'State', default='New',
        store=True)
