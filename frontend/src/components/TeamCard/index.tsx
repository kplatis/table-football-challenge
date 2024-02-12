import { Player } from '@/types/players'
import { Card, Group, Text } from '@mantine/core'
import Link from 'next/link'

type TeamCardProps = {
  name: string
  firstPlayer: Player
  secondPlayer?: Player
}

export default function TeamCard({
  name,
  firstPlayer,
  secondPlayer,
}: TeamCardProps) {
  return (
    <Card withBorder padding="lg">
      <Group justify="space-between" mt="xl">
        <Text fz="sm" fw={700}>
          {name}
        </Text>
      </Group>
      <Text mt="sm" mb="md" c="dimmed" fz="xs">
        56 km this month • 17% improvement compared to last month • 443 place in
        global scoreboard
      </Text>
      <Card.Section className="flex gap-4 justify-center">
        <div className="text-center">
          <Text size="xs" color="dimmed">
            First Player
          </Text>
          <Link href={`/teams/${firstPlayer.id}`}>
            <Text fw={500} size="sm">
              {firstPlayer.name}
            </Text>
          </Link>
        </div>
        {secondPlayer && (
          <div className="text-center">
            <Text size="xs" color="dimmed">
              Second Player
            </Text>
            <Link href={`/teams/${secondPlayer.id}`}>
              <Text fw={500} size="sm">
                {secondPlayer.name}
              </Text>
            </Link>
          </div>
        )}
      </Card.Section>
    </Card>
  )
}
