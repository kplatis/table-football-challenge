'use client'

import { Player } from '@/types/players'
import { Button, Card, Center, Group, Text } from '@mantine/core'
import classes from './TeamCard.module.css'
import { useRouter } from 'next/navigation'
import TeamBadge from '../TeamBadge'

type TeamCardProps = {
  id: number
  name: string
  firstPlayer: Player
  secondPlayer?: Player
}

export default function TeamCard({
  id,
  name,
  firstPlayer,
  secondPlayer,
}: TeamCardProps) {
  const router = useRouter()
  return (
    <Card withBorder radius="md" className={classes.card}>
      <Group justify="space-between" mt="md">
        <Text fw={800}>{name}</Text>
      </Group>

      <Card.Section className={classes.section} mt="md">
        <Text fz="sm" c="dimmed" className={classes.label}>
          Players
        </Text>

        <TeamBadge firstPlayer={firstPlayer} secondPlayer={secondPlayer} />
      </Card.Section>

      <Card.Section className={classes.section}>
        <Center>
          <Button
            size="xs"
            radius="xl"
            variant="gradient"
            gradient={{ from: 'blue', to: 'cyan', deg: 90 }}
            onClick={(e) => {
              e.preventDefault()
              router.push(`/teams/${id}`)
            }}
          >
            Visit Team Page
          </Button>
        </Center>
      </Card.Section>
    </Card>
  )
}
