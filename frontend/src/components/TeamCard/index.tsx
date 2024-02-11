import { Card, Group, Text } from '@mantine/core'

export default function TeamCard() {
  return (
    <Card withBorder padding="lg">
      <Group justify="space-between" mt="xl">
        <Text fz="sm" fw={700}>
          TEAM TITLE
        </Text>
        <Group gap={5}>
          <Text fz="xs" c="dimmed">
            80% completed
          </Text>
        </Group>
      </Group>
      <Text mt="sm" mb="md" c="dimmed" fz="xs">
        56 km this month • 17% improvement compared to last month • 443 place in
        global scoreboard
      </Text>
      <Card.Section className="flex justify-between">
        <div>
          <Text size="xs" color="dimmed">
            PLAYER 1
          </Text>
          <Text fw={500} size="sm">
            NAME 1
          </Text>
        </div>
        <div>
          <Text size="xs" color="dimmed">
            PLAYER 2
          </Text>
          <Text fw={500} size="sm">
            NAME 2
          </Text>
        </div>
      </Card.Section>
    </Card>
  )
}
