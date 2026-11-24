import random


class CommunicationNetwork:
    """
    Discrete-time communication model with message delay
    and random packet loss.
    """

    def __init__(self, delay_steps=1, packet_loss_rate=0.1, seed=7):
        if delay_steps < 0:
            raise ValueError("delay_steps cannot be negative")

        if not 0.0 <= packet_loss_rate <= 1.0:
            raise ValueError("packet_loss_rate must be between 0 and 1")

        self.delay_steps = delay_steps
        self.packet_loss_rate = packet_loss_rate
        self.rng = random.Random(seed)

        self.pending_messages = []
        self.messages_attempted = 0
        self.messages_dropped = 0
        self.messages_delivered = 0

    def send(self, sender, receiver, payload, current_step):
        self.messages_attempted += 1

        if self.rng.random() < self.packet_loss_rate:
            self.messages_dropped += 1
            return False

        self.pending_messages.append({
            "sender": sender,
            "receiver": receiver,
            "payload": payload,
            "sent_at": current_step,
            "deliver_at": current_step + self.delay_steps
        })

        return True

    def receive(self, receiver, current_step):
        delivered = []
        remaining = []

        for message in self.pending_messages:
            if (
                message["receiver"] == receiver
                and message["deliver_at"] <= current_step
            ):
                delivered.append(message)
                self.messages_delivered += 1
            else:
                remaining.append(message)

        self.pending_messages = remaining
        return delivered

    def get_statistics(self):
        return {
            "messages_attempted": self.messages_attempted,
            "messages_dropped": self.messages_dropped,
            "messages_delivered": self.messages_delivered,
            "messages_pending": len(self.pending_messages)
        }
