import PlayLiveGame from '@/components/games/PlayLiveGame'
import { Title } from '@mantine/core'

export default function LiveGamePage() {
  return (
    <>
      <Title order={1} fw={900} ta="center" m={'xl'}>
        Play a new Game
      </Title>
      <PlayLiveGame />
    </>
  )
}
