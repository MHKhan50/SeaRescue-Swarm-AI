import pytest

from searescue.communication import CommunicationNetwork


def test_message_respects_delivery_delay():
    network = CommunicationNetwork(
        delay_steps=2,
        packet_loss_rate=0,
        seed=7
    )

    assert network.send(0, 1, {"victim": (10, 5)}, 0)
    assert network.receive(1, 1) == []

    received = network.receive(1, 2)

    assert len(received) == 1
    assert received[0]["payload"]["victim"] == (10, 5)


def test_packet_loss_drops_message():
    network = CommunicationNetwork(
        delay_steps=1,
        packet_loss_rate=1.0,
        seed=7
    )

    assert not network.send(0, 1, {"victim": (10, 5)}, 0)
    assert network.receive(1, 1) == []

    stats = network.get_statistics()
    assert stats["messages_dropped"] == 1
    assert stats["messages_delivered"] == 0


def test_invalid_communication_parameters():
    with pytest.raises(ValueError):
        CommunicationNetwork(delay_steps=-1)

    with pytest.raises(ValueError):
        CommunicationNetwork(packet_loss_rate=1.5)
