'use client'

import { Player } from '@/types/players'
import { Card, Group, Title } from '@mantine/core'
import classes from './TeamCard.module.css'
import PlayerBadge from '../../players/PlayerBadge'

type TeamCardProps = {
  name: string
  firstPlayer: Player
  secondPlayer: Player | null
}

export default function TeamCard({
  name,
  firstPlayer,
  secondPlayer,
}: TeamCardProps) {
  return (
    <Card withBorder radius="md" className={classes.card}>
      <Title order={3} ta="center">
        {name}
      </Title>

      <Card.Section className={classes.section} mt="md" mb="sm">
        <Title order={4} fz="sm" c="dimmed" mb="md" fw={700}>
          PLAYERS
        </Title>
        <Group>
          <PlayerBadge name={firstPlayer.name} />
          {secondPlayer && <PlayerBadge name={secondPlayer.name} />}
        </Group>
      </Card.Section>
    </Card>
  )
}
