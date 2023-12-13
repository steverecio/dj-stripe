"""
signals are sent for each event Stripe sends to the app

Stripe docs for Webhooks: https://stripe.com/docs/webhooks
"""
from django.dispatch import Signal

# providing_args=["data", "exception"]
webhook_processing_error = Signal()

ENABLED_EVENTS = [
    # Update this by copy-pasting the "enabled_events" enum values from
    # https://raw.githubusercontent.com/stripe/openapi/master/openapi/spec3.json
    "*",
    "account.application.authorized",
    "account.application.deauthorized",
    "account.external_account.created",
    "account.external_account.deleted",
    "account.external_account.updated",
    "account.updated",
    "application_fee.created",
    "application_fee.refund.updated",
    "application_fee.refunded",
    "balance.available",
    "billing_portal.configuration.created",
    "billing_portal.configuration.updated",
    "billing_portal.session.created",
    "capability.updated",
    "cash_balance.funds_available",
    "charge.captured",
    "charge.dispute.closed",
    "charge.dispute.created",
    "charge.dispute.funds_reinstated",
    "charge.dispute.funds_withdrawn",
    "charge.dispute.updated",
    "charge.expired",
    "charge.failed",
    "charge.pending",
    "charge.refund.updated",
    "charge.refunded",
    "charge.succeeded",
    "charge.updated",
    "checkout.session.async_payment_failed",
    "checkout.session.async_payment_succeeded",
    "checkout.session.completed",
    "checkout.session.expired",
    "coupon.created",
    "coupon.deleted",
    "coupon.updated",
    "credit_note.created",
    "credit_note.updated",
    "credit_note.voided",
    "customer.created",
    "customer.deleted",
    "customer.discount.created",
    "customer.discount.deleted",
    "customer.discount.updated",
    "customer.source.created",
    "customer.source.deleted",
    "customer.source.expiring",
    "customer.source.updated",
    "customer.subscription.created",
    "customer.subscription.deleted",
    "customer.subscription.pending_update_applied",
    "customer.subscription.pending_update_expired",
    "customer.subscription.trial_will_end",
    "customer.subscription.updated",
    "customer.tax_id.created",
    "customer.tax_id.deleted",
    "customer.tax_id.updated",
    "customer.updated",
    "file.created",
    "identity.verification_session.canceled",
    "identity.verification_session.created",
    "identity.verification_session.processing",
    "identity.verification_session.redacted",
    "identity.verification_session.requires_input",
    "identity.verification_session.verified",
    "invoice.created",
    "invoice.deleted",
    "invoice.finalization_failed",
    "invoice.finalized",
    "invoice.marked_uncollectible",
    "invoice.paid",
    "invoice.payment_action_required",
    "invoice.payment_failed",
    "invoice.payment_succeeded",
    "invoice.sent",
    "invoice.upcoming",
    "invoice.updated",
    "invoice.voided",
    "invoiceitem.created",
    "invoiceitem.deleted",
    "invoiceitem.updated",
    "issuing_authorization.created",
    "issuing_authorization.request",
    "issuing_authorization.updated",
    "issuing_card.created",
    "issuing_card.updated",
    "issuing_cardholder.created",
    "issuing_cardholder.updated",
    "issuing_dispute.closed",
    "issuing_dispute.created",
    "issuing_dispute.funds_reinstated",
    "issuing_dispute.submitted",
    "issuing_dispute.updated",
    "issuing_transaction.created",
    "issuing_transaction.updated",
    "mandate.updated",
    "order.canceled",
    "order.completed",
    "order.created",
    "order.inventory_reservation_expired",
    "order.payment_completed",
    "order.payment_failed",
    "order.payment_succeeded",
    "order.processing",
    "order.reopened",
    "order.submitted",
    "order.updated",
    "order_return.created",
    "payment_intent.amount_capturable_updated",
    "payment_intent.canceled",
    "payment_intent.created",
    "payment_intent.partially_funded",
    "payment_intent.payment_failed",
    "payment_intent.processing",
    "payment_intent.requires_action",
    "payment_intent.succeeded",
    "payment_link.created",
    "payment_link.updated",
    "payment_method.attached",
    "payment_method.automatically_updated",
    "payment_method.detached",
    "payment_method.updated",
    "payout.canceled",
    "payout.created",
    "payout.failed",
    "payout.paid",
    "payout.updated",
    "person.created",
    "person.deleted",
    "person.updated",
    "plan.created",
    "plan.deleted",
    "plan.updated",
    "price.created",
    "price.deleted",
    "price.updated",
    "product.created",
    "product.deleted",
    "product.updated",
    "promotion_code.created",
    "promotion_code.updated",
    "quote.accepted",
    "quote.canceled",
    "quote.created",
    "quote.finalized",
    "radar.early_fraud_warning.created",
    "radar.early_fraud_warning.updated",
    "recipient.created",
    "recipient.deleted",
    "recipient.updated",
    "reporting.report_run.failed",
    "reporting.report_run.succeeded",
    "reporting.report_type.updated",
    "review.closed",
    "review.opened",
    "setup_intent.canceled",
    "setup_intent.created",
    "setup_intent.requires_action",
    "setup_intent.setup_failed",
    "setup_intent.succeeded",
    "sigma.scheduled_query_run.created",
    "sku.created",
    "sku.deleted",
    "sku.updated",
    "source.canceled",
    "source.chargeable",
    "source.failed",
    "source.mandate_notification",
    "source.refund_attributes_required",
    "source.transaction.created",
    "source.transaction.updated",
    "subscription_schedule.aborted",
    "subscription_schedule.canceled",
    "subscription_schedule.completed",
    "subscription_schedule.created",
    "subscription_schedule.expiring",
    "subscription_schedule.released",
    "subscription_schedule.updated",
    "tax_rate.created",
    "tax_rate.updated",
    "terminal.reader.action_failed",
    "terminal.reader.action_succeeded",
    "test_helpers.test_clock.advancing",
    "test_helpers.test_clock.created",
    "test_helpers.test_clock.deleted",
    "test_helpers.test_clock.internal_failure",
    "test_helpers.test_clock.ready",
    "topup.canceled",
    "topup.created",
    "topup.failed",
    "topup.reversed",
    "topup.succeeded",
    "transfer.created",
    "transfer.failed",
    "transfer.paid",
    "transfer.reversed",
    "transfer.updated",
    "treasury.credit_reversal.created",
    "treasury.credit_reversal.posted",
    "treasury.debit_reversal.completed",
    "treasury.debit_reversal.created",
    "treasury.debit_reversal.initial_credit_granted",
    "treasury.financial_account.closed",
    "treasury.financial_account.created",
    "treasury.financial_account.features_status_updated",
    "treasury.inbound_transfer.canceled",
    "treasury.inbound_transfer.created",
    "treasury.inbound_transfer.failed",
    "treasury.inbound_transfer.succeeded",
    "treasury.outbound_payment.canceled",
    "treasury.outbound_payment.created",
    "treasury.outbound_payment.expected_arrival_date_updated",
    "treasury.outbound_payment.failed",
    "treasury.outbound_payment.posted",
    "treasury.outbound_payment.returned",
    "treasury.outbound_transfer.canceled",
    "treasury.outbound_transfer.created",
    "treasury.outbound_transfer.expected_arrival_date_updated",
    "treasury.outbound_transfer.failed",
    "treasury.outbound_transfer.posted",
    "treasury.outbound_transfer.returned",
    "treasury.received_credit.created",
    "treasury.received_credit.failed",
    "treasury.received_credit.reversed",
    "treasury.received_credit.succeeded",
    "treasury.received_debit.created",
    # deprecated (no longer in events_types list) - TODO can be deleted?
    "checkout_beta.session_succeeded",
    "issuer_fraud_record.created",
    "payment_intent.requires_capture",
    "payment_method.card_automatically_updated",
    "issuing_dispute.created",
    "issuing_dispute.updated",
    "issuing_settlement.created",
    "issuing_settlement.updated",
    # special case? - TODO can be deleted?
    "ping",
]


# A signal for each Event type. See https://stripe.com/docs/api/events/types

WEBHOOK_SIGNALS = dict(
    [  # providing_args=["event"]
        (hook, Signal()) for hook in ENABLED_EVENTS if hook != "*"
    ]
)
